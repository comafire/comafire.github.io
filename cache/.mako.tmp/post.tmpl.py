# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1549737103.2389247
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootstrap4/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'extra_head', 'sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='ui_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        ui = _mako_get_namespace(context, 'ui')
        helper = _mako_get_namespace(context, 'helper')
        def content():
            return render_content(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        pheader = _mako_get_namespace(context, 'pheader')
        post = context.get('post', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        smartjoin = context.get('smartjoin', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        messages = context.get('messages', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        helper = _mako_get_namespace(context, 'helper')
        def content():
            return render_content(context)
        comments = _mako_get_namespace(context, 'comments')
        pheader = _mako_get_namespace(context, 'pheader')
        post = context.get('post', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        __M_writer = context.writer()
        __M_writer('\n<article class="post-')
        __M_writer(str(post.meta('type')))
        __M_writer(' h-entry hentry postpage" itemscope="itemscope" itemtype="http://schema.org/Article">\n    ')
        __M_writer(str(pheader.html_post_header()))
        __M_writer('\n    <div class="e-content entry-content" itemprop="articleBody text">\n    ')
        __M_writer(str(post.text()))
        __M_writer('\n    </div>\n    <aside class="postpromonav">\n    <nav>\n    ')
        __M_writer(str(helper.html_tags(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.html_pager(post)))
        __M_writer('\n    </nav>\n    </aside>\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('        <section class="comments hidden-print">\n        <h2>')
            __M_writer(str(messages("Comments")))
            __M_writer('</h2>\n        ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer('\n        </section>\n')
        __M_writer('    ')
        __M_writer(str(math.math_scripts_ifpost(post)))
        __M_writer('\n</article>\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        helper = _mako_get_namespace(context, 'helper')
        def extra_head():
            return render_extra_head(context)
        post = context.get('post', UNDEFINED)
        smartjoin = context.get('smartjoin', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if post.meta('keywords'):
            __M_writer('    <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(smartjoin(', ', post.meta('keywords')))))
            __M_writer('">\n')
        __M_writer('    <meta name="author" content="')
        __M_writer(filters.html_escape(str(post.author())))
        __M_writer('">\n')
        if post.prev_post:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(post.prev_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.prev_post.title())))
            __M_writer('" type="text/html">\n')
        if post.next_post:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(post.next_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.next_post.title())))
            __M_writer('" type="text/html">\n')
        if post.is_draft:
            __M_writer('        <meta name="robots" content="noindex">\n')
        __M_writer('    ')
        __M_writer(str(helper.open_graph_metadata(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.meta_translations(post)))
        __M_writer('\n    ')
        __M_writer(str(math.math_styles_ifpost(post)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        ui = _mako_get_namespace(context, 'ui')
        post = context.get('post', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if show_sourcelink:
            __M_writer('    ')
            __M_writer(str(ui.show_sourcelink(post.source_link())))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "post.tmpl", "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootstrap4/templates/post.tmpl", "source_encoding": "utf-8", "line_map": {"129": 9, "172": 27, "151": 16, "140": 9, "141": 10, "142": 10, "143": 11, "144": 12, "145": 12, "146": 12, "147": 14, "148": 14, "149": 14, "150": 15, "23": 6, "152": 16, "153": 16, "26": 3, "155": 16, "156": 18, "29": 4, "158": 19, "159": 19, "32": 2, "161": 19, "162": 21, "35": 5, "164": 24, "163": 22, "166": 24, "167": 25, "168": 25, "41": 0, "170": 26, "171": 27, "154": 16, "157": 19, "178": 53, "187": 53, "188": 54, "189": 55, "169": 26, "63": 2, "64": 3, "65": 4, "66": 5, "67": 6, "68": 7, "197": 191, "73": 28, "160": 19, "78": 51, "190": 55, "83": 57, "191": 55, "89": 30, "165": 24, "102": 30, "103": 31, "104": 31, "105": 32, "106": 32, "107": 34, "108": 34, "109": 38, "110": 38, "111": 39, "112": 39, "113": 42, "114": 43, "115": 44, "116": 44, "117": 45, "118": 45, "119": 48, "120": 48, "121": 48, "122": 50, "123": 50}}
__M_END_METADATA
"""
