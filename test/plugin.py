from mypy.types import LiteralType
from mypy.plugin import Plugin

def type_add(ctx, *args):
    lhs = ctx.type
    rhs = ctx.arg_types[0][0]
    print(lhs)
    print(rhs)
    ret = lhs.value + rhs.value
    # ctx.api.fail("test", ctx.context)
    return LiteralType(ret, fallback=ctx.api.named_generic_type('builtins.int', []))

TYPE_DICT = {
    'builtins.int.__add__': type_add
}

class TestPlugin(Plugin):

    def get_method_hook(self, fullname):
        print(fullname)
        return TYPE_DICT.get(fullname, None)

def plugin(version: str):
    return TestPlugin
