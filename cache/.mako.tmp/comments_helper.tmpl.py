# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552059405.8412657
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/comments_helper.tmpl'
_template_uri = 'comments_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link', 'comment_link_script', 'comment_form']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('isso', context._clean_inheritance_tokens(), templateuri='comments_helper_isso.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'isso')] = ns

    ns = runtime.TemplateNamespace('intensedebate', context._clean_inheritance_tokens(), templateuri='comments_helper_intensedebate.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'intensedebate')] = ns

    ns = runtime.TemplateNamespace('muut', context._clean_inheritance_tokens(), templateuri='comments_helper_muut.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'muut')] = ns

    ns = runtime.TemplateNamespace('facebook', context._clean_inheritance_tokens(), templateuri='comments_helper_facebook.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'facebook')] = ns

    ns = runtime.TemplateNamespace('commento', context._clean_inheritance_tokens(), templateuri='comments_helper_commento.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'commento')] = ns

    ns = runtime.TemplateNamespace('disqus', context._clean_inheritance_tokens(), templateuri='comments_helper_disqus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'disqus')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        isso = _mako_get_namespace(context, 'isso')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        muut = _mako_get_namespace(context, 'muut')
        facebook = _mako_get_namespace(context, 'facebook')
        commento = _mako_get_namespace(context, 'commento')
        disqus = _mako_get_namespace(context, 'disqus')
        comment_system = context.get('comment_system', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system == 'disqus':
            __M_writer('        ')
            __M_writer(str(disqus.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'intensedebate':
            __M_writer('        ')
            __M_writer(str(intensedebate.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'muut':
            __M_writer('        ')
            __M_writer(str(muut.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'facebook':
            __M_writer('        ')
            __M_writer(str(facebook.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'isso':
            __M_writer('        ')
            __M_writer(str(isso.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'commento':
            __M_writer('        ')
            __M_writer(str(commento.comment_link(link, identifier)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        isso = _mako_get_namespace(context, 'isso')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        muut = _mako_get_namespace(context, 'muut')
        facebook = _mako_get_namespace(context, 'facebook')
        commento = _mako_get_namespace(context, 'commento')
        disqus = _mako_get_namespace(context, 'disqus')
        comment_system = context.get('comment_system', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system == 'disqus':
            __M_writer('        ')
            __M_writer(str(disqus.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'intensedebate':
            __M_writer('        ')
            __M_writer(str(intensedebate.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'muut':
            __M_writer('        ')
            __M_writer(str(muut.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'facebook':
            __M_writer('        ')
            __M_writer(str(facebook.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'isso':
            __M_writer('        ')
            __M_writer(str(isso.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'commento':
            __M_writer('        ')
            __M_writer(str(commento.comment_link_script()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        isso = _mako_get_namespace(context, 'isso')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        muut = _mako_get_namespace(context, 'muut')
        facebook = _mako_get_namespace(context, 'facebook')
        commento = _mako_get_namespace(context, 'commento')
        disqus = _mako_get_namespace(context, 'disqus')
        comment_system = context.get('comment_system', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system == 'disqus':
            __M_writer('        ')
            __M_writer(str(disqus.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'intensedebate':
            __M_writer('        ')
            __M_writer(str(intensedebate.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'muut':
            __M_writer('        ')
            __M_writer(str(muut.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'facebook':
            __M_writer('        ')
            __M_writer(str(facebook.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'isso':
            __M_writer('        ')
            __M_writer(str(isso.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'commento':
            __M_writer('        ')
            __M_writer(str(commento.comment_form(url, title, identifier)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"23": 7, "26": 4, "29": 5, "32": 6, "35": 8, "38": 3, "41": 0, "46": 2, "47": 3, "48": 4, "49": 5, "50": 6, "51": 7, "52": 8, "53": 24, "54": 40, "55": 56, "61": 26, "72": 26, "73": 27, "74": 28, "75": 28, "76": 28, "77": 29, "78": 30, "79": 30, "80": 30, "81": 31, "82": 32, "83": 32, "84": 32, "85": 33, "86": 34, "87": 34, "88": 34, "89": 35, "90": 36, "91": 36, "92": 36, "93": 37, "94": 38, "95": 38, "96": 38, "102": 42, "113": 42, "114": 43, "115": 44, "116": 44, "117": 44, "118": 45, "119": 46, "120": 46, "121": 46, "122": 47, "123": 48, "124": 48, "125": 48, "126": 49, "127": 50, "128": 50, "129": 50, "130": 51, "131": 52, "132": 52, "133": 52, "134": 53, "135": 54, "136": 54, "137": 54, "143": 10, "154": 10, "155": 11, "156": 12, "157": 12, "158": 12, "159": 13, "160": 14, "161": 14, "162": 14, "163": 15, "164": 16, "165": 16, "166": 16, "167": 17, "168": 18, "169": 18, "170": 18, "171": 19, "172": 20, "173": 20, "174": 20, "175": 21, "176": 22, "177": 22, "178": 22, "184": 178}, "uri": "comments_helper.tmpl", "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/comments_helper.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
