# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552059592.989137
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/comments_helper.tmpl'
_template_uri = 'comments_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link', 'comment_form', 'comment_link_script']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('intensedebate', context._clean_inheritance_tokens(), templateuri='comments_helper_intensedebate.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'intensedebate')] = ns

    ns = runtime.TemplateNamespace('isso', context._clean_inheritance_tokens(), templateuri='comments_helper_isso.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'isso')] = ns

    ns = runtime.TemplateNamespace('disqus', context._clean_inheritance_tokens(), templateuri='comments_helper_disqus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'disqus')] = ns

    ns = runtime.TemplateNamespace('commento', context._clean_inheritance_tokens(), templateuri='comments_helper_commento.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'commento')] = ns

    ns = runtime.TemplateNamespace('muut', context._clean_inheritance_tokens(), templateuri='comments_helper_muut.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'muut')] = ns

    ns = runtime.TemplateNamespace('facebook', context._clean_inheritance_tokens(), templateuri='comments_helper_facebook.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'facebook')] = ns

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
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        muut = _mako_get_namespace(context, 'muut')
        comment_system = context.get('comment_system', UNDEFINED)
        disqus = _mako_get_namespace(context, 'disqus')
        isso = _mako_get_namespace(context, 'isso')
        commento = _mako_get_namespace(context, 'commento')
        facebook = _mako_get_namespace(context, 'facebook')
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


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        muut = _mako_get_namespace(context, 'muut')
        comment_system = context.get('comment_system', UNDEFINED)
        disqus = _mako_get_namespace(context, 'disqus')
        isso = _mako_get_namespace(context, 'isso')
        commento = _mako_get_namespace(context, 'commento')
        facebook = _mako_get_namespace(context, 'facebook')
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
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        muut = _mako_get_namespace(context, 'muut')
        isso = _mako_get_namespace(context, 'isso')
        comment_system = context.get('comment_system', UNDEFINED)
        disqus = _mako_get_namespace(context, 'disqus')
        commento = _mako_get_namespace(context, 'commento')
        facebook = _mako_get_namespace(context, 'facebook')
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


"""
__M_BEGIN_METADATA
{"filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/comments_helper.tmpl", "source_encoding": "utf-8", "line_map": {"23": 4, "26": 7, "29": 3, "32": 8, "35": 5, "38": 6, "41": 0, "46": 2, "47": 3, "48": 4, "49": 5, "50": 6, "51": 7, "52": 8, "53": 24, "54": 40, "55": 56, "61": 26, "72": 26, "73": 27, "74": 28, "75": 28, "76": 28, "77": 29, "78": 30, "79": 30, "80": 30, "81": 31, "82": 32, "83": 32, "84": 32, "85": 33, "86": 34, "87": 34, "88": 34, "89": 35, "90": 36, "91": 36, "92": 36, "93": 37, "94": 38, "95": 38, "96": 38, "102": 10, "113": 10, "114": 11, "115": 12, "116": 12, "117": 12, "118": 13, "119": 14, "120": 14, "121": 14, "122": 15, "123": 16, "124": 16, "125": 16, "126": 17, "127": 18, "128": 18, "129": 18, "130": 19, "131": 20, "132": 20, "133": 20, "134": 21, "135": 22, "136": 22, "137": 22, "143": 42, "154": 42, "155": 43, "156": 44, "157": 44, "158": 44, "159": 45, "160": 46, "161": 46, "162": 46, "163": 47, "164": 48, "165": 48, "166": 48, "167": 49, "168": 50, "169": 50, "170": 50, "171": 51, "172": 52, "173": 52, "174": 52, "175": 53, "176": 54, "177": 54, "178": 54, "184": 178}, "uri": "comments_helper.tmpl"}
__M_END_METADATA
"""
