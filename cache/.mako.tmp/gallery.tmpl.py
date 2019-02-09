# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1549728374.8883157
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootstrap4/templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_js', 'content', 'extra_head', 'sourcelink']


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
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        thumbnail_size = context.get('thumbnail_size', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        photo_array = context.get('photo_array', UNDEFINED)
        photo_array_json = context.get('photo_array_json', UNDEFINED)
        folders = context.get('folders', UNDEFINED)
        title = context.get('title', UNDEFINED)
        post = context.get('post', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        ui = _mako_get_namespace(context, 'ui')
        comments = _mako_get_namespace(context, 'comments')
        enable_comments = context.get('enable_comments', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        gallery_path = context.get('gallery_path', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
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


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_js():
            return render_extra_js(context)
        thumbnail_size = context.get('thumbnail_size', UNDEFINED)
        photo_array_json = context.get('photo_array_json', UNDEFINED)
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
        post = context.get('post', UNDEFINED)
        folders = context.get('folders', UNDEFINED)
        ui = _mako_get_namespace(context, 'ui')
        def content():
            return render_content(context)
        crumbs = context.get('crumbs', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        enable_comments = context.get('enable_comments', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        photo_array = context.get('photo_array', UNDEFINED)
        title = context.get('title', UNDEFINED)
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


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        gallery_path = context.get('gallery_path', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
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


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"128": 9, "129": 10, "130": 10, "131": 10, "132": 12, "133": 13, "134": 14, "135": 14, "136": 17, "137": 18, "138": 19, "139": 20, "140": 20, "141": 20, "142": 20, "143": 20, "144": 22, "145": 24, "146": 26, "147": 27, "148": 29, "149": 30, "150": 30, "23": 3, "152": 30, "153": 30, "26": 4, "155": 31, "156": 31, "154": 31, "158": 33, "159": 36, "32": 0, "161": 37, "167": 41, "157": 31, "179": 41, "180": 42, "181": 42, "182": 52, "183": 53, "184": 54, "185": 55, "186": 55, "187": 55, "151": 30, "189": 55, "63": 2, "64": 3, "65": 4, "195": 5, "70": 5, "75": 39, "206": 195, "80": 59, "85": 70, "91": 61, "99": 61, "100": 65, "101": 65, "102": 66, "103": 66, "188": 55, "109": 7, "160": 37, "125": 7, "126": 8, "127": 8}, "source_encoding": "utf-8", "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootstrap4/templates/gallery.tmpl", "uri": "gallery.tmpl"}
__M_END_METADATA
"""
