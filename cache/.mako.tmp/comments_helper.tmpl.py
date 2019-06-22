# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1561218957.4951384
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/comments_helper.tmpl'
_template_uri = 'comments_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link_script', 'comment_form', 'comment_link']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('disqus', context._clean_inheritance_tokens(), templateuri='comments_helper_disqus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'disqus')] = ns

    ns = runtime.TemplateNamespace('muut', context._clean_inheritance_tokens(), templateuri='comments_helper_muut.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'muut')] = ns

    ns = runtime.TemplateNamespace('isso', context._clean_inheritance_tokens(), templateuri='comments_helper_isso.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'isso')] = ns

    ns = runtime.TemplateNamespace('commento', context._clean_inheritance_tokens(), templateuri='comments_helper_commento.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'commento')] = ns

    ns = runtime.TemplateNamespace('facebook', context._clean_inheritance_tokens(), templateuri='comments_helper_facebook.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'facebook')] = ns

    ns = runtime.TemplateNamespace('intensedebate', context._clean_inheritance_tokens(), templateuri='comments_helper_intensedebate.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'intensedebate')] = ns

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


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        disqus = _mako_get_namespace(context, 'disqus')
        comment_system = context.get('comment_system', UNDEFINED)
        facebook = _mako_get_namespace(context, 'facebook')
        isso = _mako_get_namespace(context, 'isso')
        commento = _mako_get_namespace(context, 'commento')
        muut = _mako_get_namespace(context, 'muut')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
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
        disqus = _mako_get_namespace(context, 'disqus')
        comment_system = context.get('comment_system', UNDEFINED)
        facebook = _mako_get_namespace(context, 'facebook')
        isso = _mako_get_namespace(context, 'isso')
        commento = _mako_get_namespace(context, 'commento')
        muut = _mako_get_namespace(context, 'muut')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
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


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        disqus = _mako_get_namespace(context, 'disqus')
        comment_system = context.get('comment_system', UNDEFINED)
        facebook = _mako_get_namespace(context, 'facebook')
        isso = _mako_get_namespace(context, 'isso')
        commento = _mako_get_namespace(context, 'commento')
        muut = _mako_get_namespace(context, 'muut')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
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


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"23": 3, "26": 5, "29": 7, "32": 8, "35": 6, "38": 4, "41": 0, "46": 2, "47": 3, "48": 4, "49": 5, "50": 6, "51": 7, "52": 8, "53": 24, "54": 40, "55": 56, "61": 42, "72": 42, "73": 43, "74": 44, "75": 44, "76": 44, "77": 45, "78": 46, "79": 46, "80": 46, "81": 47, "82": 48, "83": 48, "84": 48, "85": 49, "86": 50, "87": 50, "88": 50, "89": 51, "90": 52, "91": 52, "92": 52, "93": 53, "94": 54, "95": 54, "96": 54, "102": 10, "113": 10, "114": 11, "115": 12, "116": 12, "117": 12, "118": 13, "119": 14, "120": 14, "121": 14, "122": 15, "123": 16, "124": 16, "125": 16, "126": 17, "127": 18, "128": 18, "129": 18, "130": 19, "131": 20, "132": 20, "133": 20, "134": 21, "135": 22, "136": 22, "137": 22, "143": 26, "154": 26, "155": 27, "156": 28, "157": 28, "158": 28, "159": 29, "160": 30, "161": 30, "162": 30, "163": 31, "164": 32, "165": 32, "166": 32, "167": 33, "168": 34, "169": 34, "170": 34, "171": 35, "172": 36, "173": 36, "174": 36, "175": 37, "176": 38, "177": 38, "178": 38, "184": 178}, "uri": "comments_helper.tmpl", "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/comments_helper.tmpl"}
__M_END_METADATA
"""
