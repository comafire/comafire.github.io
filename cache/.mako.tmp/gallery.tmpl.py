# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555821164.8339546
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootstrap4/templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'sourcelink', 'content', 'extra_js']


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
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        permalink = context.get('permalink', UNDEFINED)
        title = context.get('title', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        post = context.get('post', UNDEFINED)
        ui = _mako_get_namespace(context, 'ui')
        len = context.get('len', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        enable_comments = context.get('enable_comments', UNDEFINED)
        photo_array = context.get('photo_array', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        thumbnail_size = context.get('thumbnail_size', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        photo_array_json = context.get('photo_array_json', UNDEFINED)
        folders = context.get('folders', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        gallery_path = context.get('gallery_path', UNDEFINED)
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


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        lang = context.get('lang', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        gallery_path = context.get('gallery_path', UNDEFINED)
        len = context.get('len', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        enable_comments = context.get('enable_comments', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        photo_array = context.get('photo_array', UNDEFINED)
        title = context.get('title', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        folders = context.get('folders', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        post = context.get('post', UNDEFINED)
        ui = _mako_get_namespace(context, 'ui')
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


"""
__M_BEGIN_METADATA
{"line_map": {"130": 7, "151": 10, "175": 31, "146": 7, "147": 8, "148": 8, "149": 9, "150": 10, "23": 3, "152": 10, "153": 12, "26": 4, "155": 14, "156": 14, "154": 13, "158": 18, "159": 19, "32": 0, "161": 20, "162": 20, "163": 20, "164": 20, "165": 22, "166": 24, "167": 26, "168": 27, "169": 29, "170": 30, "171": 30, "172": 30, "173": 30, "174": 30, "157": 17, "176": 31, "177": 31, "178": 31, "179": 33, "180": 36, "181": 37, "182": 37, "188": 61, "63": 2, "64": 3, "65": 4, "196": 61, "197": 65, "70": 5, "199": 66, "200": 66, "75": 39, "206": 200, "80": 59, "85": 70, "91": 41, "198": 65, "103": 41, "104": 42, "105": 42, "106": 52, "107": 53, "108": 54, "109": 55, "110": 55, "111": 55, "112": 55, "113": 55, "119": 5, "160": 20}, "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootstrap4/templates/gallery.tmpl", "uri": "gallery.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
