# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1557925262.3488066
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootstrap4/templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'extra_js', 'sourcelink']


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
        crumbs = context.get('crumbs', UNDEFINED)
        enable_comments = context.get('enable_comments', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        thumbnail_size = context.get('thumbnail_size', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        gallery_path = context.get('gallery_path', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        permalink = context.get('permalink', UNDEFINED)
        photo_array_json = context.get('photo_array_json', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        title = context.get('title', UNDEFINED)
        len = context.get('len', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        folders = context.get('folders', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        post = context.get('post', UNDEFINED)
        photo_array = context.get('photo_array', UNDEFINED)
        ui = _mako_get_namespace(context, 'ui')
        _link = context.get('_link', UNDEFINED)
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
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
        translations = context.get('translations', UNDEFINED)
        gallery_path = context.get('gallery_path', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        parent = context.get('parent', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        crumbs = context.get('crumbs', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        enable_comments = context.get('enable_comments', UNDEFINED)
        def content():
            return render_content(context)
        post = context.get('post', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        photo_array = context.get('photo_array', UNDEFINED)
        title = context.get('title', UNDEFINED)
        ui = _mako_get_namespace(context, 'ui')
        folders = context.get('folders', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
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
        def extra_js():
            return render_extra_js(context)
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
{"filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootstrap4/templates/gallery.tmpl", "source_encoding": "utf-8", "line_map": {"135": 7, "136": 8, "137": 8, "138": 9, "139": 10, "140": 10, "141": 10, "142": 12, "143": 13, "144": 14, "145": 14, "146": 17, "147": 18, "148": 19, "149": 20, "150": 20, "23": 3, "152": 20, "153": 20, "26": 4, "155": 24, "156": 26, "154": 22, "158": 29, "159": 30, "32": 0, "161": 30, "162": 30, "163": 30, "164": 31, "165": 31, "166": 31, "167": 31, "168": 33, "169": 36, "170": 37, "171": 37, "157": 27, "177": 61, "185": 61, "186": 65, "187": 65, "151": 20, "189": 66, "63": 2, "64": 3, "65": 4, "195": 5, "70": 5, "75": 39, "206": 195, "80": 59, "85": 70, "91": 41, "188": 66, "103": 41, "104": 42, "105": 42, "106": 52, "107": 53, "108": 54, "109": 55, "110": 55, "111": 55, "112": 55, "113": 55, "119": 7, "160": 30}, "uri": "gallery.tmpl"}
__M_END_METADATA
"""
