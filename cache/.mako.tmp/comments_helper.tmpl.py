# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1558368497.5708618
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/comments_helper.tmpl'
_template_uri = 'comments_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link_script', 'comment_link']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('commento', context._clean_inheritance_tokens(), templateuri='comments_helper_commento.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'commento')] = ns

    ns = runtime.TemplateNamespace('muut', context._clean_inheritance_tokens(), templateuri='comments_helper_muut.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'muut')] = ns

    ns = runtime.TemplateNamespace('facebook', context._clean_inheritance_tokens(), templateuri='comments_helper_facebook.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'facebook')] = ns

    ns = runtime.TemplateNamespace('intensedebate', context._clean_inheritance_tokens(), templateuri='comments_helper_intensedebate.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'intensedebate')] = ns

    ns = runtime.TemplateNamespace('isso', context._clean_inheritance_tokens(), templateuri='comments_helper_isso.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'isso')] = ns

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


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        commento = _mako_get_namespace(context, 'commento')
        muut = _mako_get_namespace(context, 'muut')
        comment_system = context.get('comment_system', UNDEFINED)
        facebook = _mako_get_namespace(context, 'facebook')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        isso = _mako_get_namespace(context, 'isso')
        disqus = _mako_get_namespace(context, 'disqus')
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


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        commento = _mako_get_namespace(context, 'commento')
        muut = _mako_get_namespace(context, 'muut')
        comment_system = context.get('comment_system', UNDEFINED)
        facebook = _mako_get_namespace(context, 'facebook')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        isso = _mako_get_namespace(context, 'isso')
        disqus = _mako_get_namespace(context, 'disqus')
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


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        commento = _mako_get_namespace(context, 'commento')
        muut = _mako_get_namespace(context, 'muut')
        comment_system = context.get('comment_system', UNDEFINED)
        facebook = _mako_get_namespace(context, 'facebook')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        isso = _mako_get_namespace(context, 'isso')
        disqus = _mako_get_namespace(context, 'disqus')
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
{"source_encoding": "utf-8", "uri": "comments_helper.tmpl", "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/comments_helper.tmpl", "line_map": {"23": 8, "26": 5, "29": 6, "32": 4, "35": 7, "38": 3, "41": 0, "46": 2, "47": 3, "48": 4, "49": 5, "50": 6, "51": 7, "52": 8, "53": 24, "54": 40, "55": 56, "61": 10, "72": 10, "73": 11, "74": 12, "75": 12, "76": 12, "77": 13, "78": 14, "79": 14, "80": 14, "81": 15, "82": 16, "83": 16, "84": 16, "85": 17, "86": 18, "87": 18, "88": 18, "89": 19, "90": 20, "91": 20, "92": 20, "93": 21, "94": 22, "95": 22, "96": 22, "102": 42, "113": 42, "114": 43, "115": 44, "116": 44, "117": 44, "118": 45, "119": 46, "120": 46, "121": 46, "122": 47, "123": 48, "124": 48, "125": 48, "126": 49, "127": 50, "128": 50, "129": 50, "130": 51, "131": 52, "132": 52, "133": 52, "134": 53, "135": 54, "136": 54, "137": 54, "143": 26, "154": 26, "155": 27, "156": 28, "157": 28, "158": 28, "159": 29, "160": 30, "161": 30, "162": 30, "163": 31, "164": 32, "165": 32, "166": 32, "167": 33, "168": 34, "169": 34, "170": 34, "171": 35, "172": 36, "173": 36, "174": 36, "175": 37, "176": 38, "177": 38, "178": 38, "184": 178}}
__M_END_METADATA
"""
