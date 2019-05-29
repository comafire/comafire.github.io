# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1559147898.4773178
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/comments_helper.tmpl'
_template_uri = 'comments_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link_script', 'comment_link', 'comment_form']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('isso', context._clean_inheritance_tokens(), templateuri='comments_helper_isso.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'isso')] = ns

    ns = runtime.TemplateNamespace('disqus', context._clean_inheritance_tokens(), templateuri='comments_helper_disqus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'disqus')] = ns

    ns = runtime.TemplateNamespace('muut', context._clean_inheritance_tokens(), templateuri='comments_helper_muut.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'muut')] = ns

    ns = runtime.TemplateNamespace('commento', context._clean_inheritance_tokens(), templateuri='comments_helper_commento.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'commento')] = ns

    ns = runtime.TemplateNamespace('intensedebate', context._clean_inheritance_tokens(), templateuri='comments_helper_intensedebate.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'intensedebate')] = ns

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


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        isso = _mako_get_namespace(context, 'isso')
        disqus = _mako_get_namespace(context, 'disqus')
        muut = _mako_get_namespace(context, 'muut')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        commento = _mako_get_namespace(context, 'commento')
        comment_system = context.get('comment_system', UNDEFINED)
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


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        isso = _mako_get_namespace(context, 'isso')
        disqus = _mako_get_namespace(context, 'disqus')
        muut = _mako_get_namespace(context, 'muut')
        commento = _mako_get_namespace(context, 'commento')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        comment_system = context.get('comment_system', UNDEFINED)
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
        isso = _mako_get_namespace(context, 'isso')
        disqus = _mako_get_namespace(context, 'disqus')
        muut = _mako_get_namespace(context, 'muut')
        commento = _mako_get_namespace(context, 'commento')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        comment_system = context.get('comment_system', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"uri": "comments_helper.tmpl", "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/comments_helper.tmpl", "line_map": {"23": 7, "26": 3, "29": 5, "32": 8, "35": 4, "38": 6, "41": 0, "46": 2, "47": 3, "48": 4, "49": 5, "50": 6, "51": 7, "52": 8, "53": 24, "54": 40, "55": 56, "61": 42, "72": 42, "73": 43, "74": 44, "75": 44, "76": 44, "77": 45, "78": 46, "79": 46, "80": 46, "81": 47, "82": 48, "83": 48, "84": 48, "85": 49, "86": 50, "87": 50, "88": 50, "89": 51, "90": 52, "91": 52, "92": 52, "93": 53, "94": 54, "95": 54, "96": 54, "102": 26, "113": 26, "114": 27, "115": 28, "116": 28, "117": 28, "118": 29, "119": 30, "120": 30, "121": 30, "122": 31, "123": 32, "124": 32, "125": 32, "126": 33, "127": 34, "128": 34, "129": 34, "130": 35, "131": 36, "132": 36, "133": 36, "134": 37, "135": 38, "136": 38, "137": 38, "143": 10, "154": 10, "155": 11, "156": 12, "157": 12, "158": 12, "159": 13, "160": 14, "161": 14, "162": 14, "163": 15, "164": 16, "165": 16, "166": 16, "167": 17, "168": 18, "169": 18, "170": 18, "171": 19, "172": 20, "173": 20, "174": 20, "175": 21, "176": 22, "177": 22, "178": 22, "184": 178}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
