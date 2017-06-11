from inspect import signature
def demo(args1:'int < 0', arg2:str = 'default') -> str:
    pass
if __name__ == '__main__':
    sig = signature(demo)
    print (str(sig))
    for name, param in sig.parameters.items():
        print (param.kind,':',name,'=',param.default)
    sig.bind(30)
    try:
        sig.bind()
    except TypeError:
        raise

