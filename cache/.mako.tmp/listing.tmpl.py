# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1557937456.0506716
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootstrap4/templates/listing.tmpl'
_template_uri = 'listing.tmpl'
_source_encoding = 'utf-8'
_exports = ['sourcelink', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='ui_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        source_link = context.get('source_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        code = context.get('code', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        ui = _mako_get_namespace(context, 'ui')
        title = context.get('title', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        folders = context.get('folders', UNDEFINED)
        files = context.get('files', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        source_link = context.get('source_link', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context)
        ui = _mako_get_namespace(context, 'ui')
        __M_writer = context.writer()
        __M_writer('\n')
        if source_link and show_sourcelink:
            __M_writer('    ')
            __M_writer(str(ui.show_sourcelink(source_link)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        source_link = context.get('source_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def content():
            return render_content(context)
        code = context.get('code', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        ui = _mako_get_namespace(context, 'ui')
        title = context.get('title', UNDEFINED)
        folders = context.get('folders', UNDEFINED)
        files = context.get('files', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(ui.breadcrumbs(crumbs)))
        __M_writer('\n')
        if folders or files:
            __M_writer('<ul>\n')
            for name in folders:
                __M_writer('    <li><a href="')
                __M_writer(filters.url_escape(str(name)))
                __M_writer('">📂&nbsp;')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a>\n')
            for name in files:
                __M_writer('    <li><a href="')
                __M_writer(filters.url_escape(str(name)))
                __M_writer('.html">📄&nbsp;')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a>\n')
            __M_writer('</ul>\n')
        if code:
            __M_writer('<h1>')
            __M_writer(str(title))
            __M_writer('\n')
            if source_link:
                __M_writer('        <small><a href="')
                __M_writer(str(source_link))
                __M_writer('">(')
                __M_writer(str(messages("Source")))
                __M_writer(')</a></small>\n')
            __M_writer('    </h1>\n    ')
            __M_writer(str(code))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "listing.tmpl", "line_map": {"133": 127, "23": 3, "29": 0, "47": 2, "48": 3, "53": 24, "58": 30, "64": 26, "73": 26, "74": 27, "75": 28, "76": 28, "77": 28, "83": 4, "97": 4, "98": 5, "99": 5, "100": 6, "101": 7, "102": 8, "103": 9, "104": 9, "105": 9, "106": 9, "107": 9, "108": 11, "109": 12, "110": 12, "111": 12, "112": 12, "113": 12, "114": 14, "115": 16, "116": 17, "117": 17, "118": 17, "119": 18, "120": 19, "121": 19, "122": 19, "123": 19, "124": 19, "125": 21, "126": 22, "127": 22}, "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootstrap4/templates/listing.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
