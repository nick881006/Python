# encoding=utf-8


# 判断每个文本块加什么标记
# 规则父类
class Rule:
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True

# 一号标题规则
class HeadingRule(Rule):
    type = 'heading'

    # 判断文本块是否符合规则
    def condition(self, block):
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'

# 二号标题规则
class TitleRule(HeadingRule):
    type = 'title'
    first = True

    def condition(self, block):
        if not self.first: return False
        self.first = False
        return HeadingRule.condition(self, block);

# 列表项规则
class ListItemRule(Rule):
    type = 'listitem'

    def condition(self, block):
        return block[0] == '-'

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True

# 列表规则
class ListRule(ListItemRule):
    type = 'list'
    inside = False

    def condition(self, block):
        return True

    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False

# 段落规则
class ParagraphRule(Rule):
    type = 'paragraph'

    def condition(self, block):
        return True