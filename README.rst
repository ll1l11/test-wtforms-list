Test Flask-WTF List
===================

如下的数据 

    {'tags': ['a;, ‘b’]}

FieldList兑现处理主要处理

例如我们有如下的form:

    class TagForm(Form):
        tags = FieldList(StringField('tag'), min_entries=2)


那么我要传输上面的数据, 则需要传这样的数据格式:

    tags-0=one&tags-1=two


这显然不是我们想要的
