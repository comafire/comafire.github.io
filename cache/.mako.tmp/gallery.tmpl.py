# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1550250704.522861
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootstrap4/templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_js', 'sourcelink', 'content', 'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='ui_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        gallery_path = context.get('gallery_path', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        thumbnail_size = context.get('thumbnail_size', UNDEFINED)
        ui = _mako_get_namespace(context, 'ui')
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        translations = context.get('translations', UNDEFINED)
        photo_array = context.get('photo_array', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        enable_comments = context.get('enable_comments', UNDEFINED)
        photo_array_json = context.get('photo_array_json', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        title = context.get('title', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        parent = context.get('parent', UNDEFINED)
        folders = context.get('folders', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        len = context.get('len', UNDEFINED)
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
        photo_array_json = context.get('photo_array_json', UNDEFINED)
        def extra_js():
            return render_extra_js(context)
        thumbnail_size = context.get('thumbnail_size', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        enable_comments = context.get('enable_comments', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        title = context.get('title', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        ui = _mako_get_namespace(context, 'ui')
        folders = context.get('folders', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        photo_array = context.get('photo_array', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
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
        gallery_path = context.get('gallery_path', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        parent = context.get('parent', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootstrap4/templates/gallery.tmpl", "source_encoding": "utf-8", "line_map": {"192": 42, "193": 52, "136": 7, "137": 8, "138": 8, "139": 9, "140": 10, "141": 10, "142": 10, "143": 12, "144": 13, "145": 14, "146": 14, "147": 17, "148": 18, "149": 19, "150": 20, "23": 4, "152": 20, "153": 20, "26": 3, "155": 22, "156": 24, "154": 20, "158": 27, "159": 29, "32": 0, "161": 30, "162": 30, "163": 30, "164": 30, "165": 31, "166": 31, "167": 31, "168": 31, "169": 33, "170": 36, "171": 37, "172": 37, "157": 26, "178": 41, "151": 20, "190": 41, "63": 2, "64": 3, "65": 4, "194": 53, "195": 54, "196": 55, "197": 55, "70": 5, "199": 55, "200": 55, "75": 39, "206": 200, "80": 59, "85": 70, "160": 30, "91": 61, "198": 55, "99": 61, "100": 65, "101": 65, "102": 66, "103": 66, "109": 5, "120": 7, "191": 42}, "uri": "gallery.tmpl"}
__M_END_METADATA
"""
