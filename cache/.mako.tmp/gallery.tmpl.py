# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1549736482.7364733
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootstrap4/templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = ['sourcelink', 'extra_head', 'extra_js', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='ui_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        len = context.get('len', UNDEFINED)
        photo_array = context.get('photo_array', UNDEFINED)
        folders = context.get('folders', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        thumbnail_size = context.get('thumbnail_size', UNDEFINED)
        ui = _mako_get_namespace(context, 'ui')
        gallery_path = context.get('gallery_path', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        title = context.get('title', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        photo_array_json = context.get('photo_array_json', UNDEFINED)
        enable_comments = context.get('enable_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        parent = context.get('parent', UNDEFINED)
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        translations = context.get('translations', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        parent = context.get('parent', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        gallery_path = context.get('gallery_path', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n<link rel="alternate" type="application/rss+xml" title="RSS" href="rss.xml">\n<style type="text/css">\n    #gallery_container {\n        position: relative;\n    }\n    .image-block {\n        position: absolute;\n    }\n</style>\n')
        if len(translations) > 1:
            for langname in translations.keys():
                if langname != lang:
                    __M_writer('             <link rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('" href="')
                    __M_writer(str(_link('gallery', gallery_path, langname)))
                    __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        thumbnail_size = context.get('thumbnail_size', UNDEFINED)
        photo_array_json = context.get('photo_array_json', UNDEFINED)
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        __M_writer('\n<script src="/assets/js/justified-layout.min.js"></script>\n<script src="/assets/js/gallery.min.js"></script>\n<script>\nvar jsonContent = ')
        __M_writer(str(photo_array_json))
        __M_writer(';\nvar thumbnailSize = ')
        __M_writer(str(thumbnail_size))
        __M_writer(";\nrenderGallery(jsonContent, thumbnailSize);\nwindow.addEventListener('resize', renderGallery);\n</script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        photo_array = context.get('photo_array', UNDEFINED)
        folders = context.get('folders', UNDEFINED)
        enable_comments = context.get('enable_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        ui = _mako_get_namespace(context, 'ui')
        permalink = context.get('permalink', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(ui.breadcrumbs(crumbs)))
        __M_writer('\n')
        if title:
            __M_writer('    <h1>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\n')
        if post:
            __M_writer('    <p>\n        ')
            __M_writer(str(post.text()))
            __M_writer('\n    </p>\n')
        if folders:
            __M_writer('    <ul>\n')
            for folder, ftitle in folders:
                __M_writer('        <li><a href="')
                __M_writer(str(folder))
                __M_writer('">📂&nbsp;')
                __M_writer(filters.html_escape(str(ftitle)))
                __M_writer('</a></li>\n')
            __M_writer('    </ul>\n')
        __M_writer('\n<div id="gallery_container"></div>\n')
        if photo_array:
            __M_writer('<noscript>\n<ul class="thumbnails">\n')
            for image in photo_array:
                __M_writer('        <li><a href="')
                __M_writer(str(image['url']))
                __M_writer('" class="thumbnail image-reference" title="')
                __M_writer(filters.html_escape(str(image['title'])))
                __M_writer('">\n            <img src="')
                __M_writer(str(image['url_thumb']))
                __M_writer('" alt="')
                __M_writer(filters.html_escape(str(image['title'])))
                __M_writer('" /></a>\n')
            __M_writer('</ul>\n</noscript>\n')
        if site_has_comments and enable_comments:
            __M_writer(str(comments.comment_form(None, permalink, title)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootstrap4/templates/gallery.tmpl", "uri": "gallery.tmpl", "source_encoding": "utf-8", "line_map": {"192": 30, "130": 61, "193": 31, "138": 61, "139": 65, "140": 65, "141": 66, "142": 66, "148": 7, "23": 3, "26": 4, "32": 0, "164": 7, "165": 8, "166": 8, "167": 9, "168": 10, "169": 10, "170": 10, "171": 12, "172": 13, "173": 14, "174": 14, "175": 17, "176": 18, "177": 19, "178": 20, "179": 20, "180": 20, "181": 20, "182": 20, "183": 22, "184": 24, "185": 26, "186": 27, "187": 29, "188": 30, "189": 30, "190": 30, "63": 2, "64": 3, "65": 4, "194": 31, "195": 31, "196": 31, "197": 33, "70": 5, "199": 37, "200": 37, "75": 39, "206": 200, "80": 59, "85": 70, "91": 5, "198": 36, "102": 41, "191": 30, "114": 41, "115": 42, "116": 42, "117": 52, "118": 53, "119": 54, "120": 55, "121": 55, "122": 55, "123": 55, "124": 55}}
__M_END_METADATA
"""
