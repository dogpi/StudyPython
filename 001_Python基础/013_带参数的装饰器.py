

def outer(say):
    def inner(name):
        if name=="dogpi":
            say(name)
        else:
            name="catpi"
            say(name)
    return inner

@outer
def say(name):
    print("%s is a good man"%(name))


# outer(say)("dogpi1")

say("dopcat")