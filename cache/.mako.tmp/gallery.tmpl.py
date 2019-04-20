# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555773022.6677873
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootstrap4/templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'extra_head', 'extra_js', 'sourcelink']


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
        parent = context.get('parent', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        title = context.get('title', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        photo_array = context.get('photo_array', UNDEFINED)
        gallery_path = context.get('gallery_path', UNDEFINED)
        ui = _mako_get_namespace(context, 'ui')
        translations = context.get('translations', UNDEFINED)
        post = context.get('post', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        len = context.get('len', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        folders = context.get('folders', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        thumbnail_size = context.get('thumbnail_size', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        photo_array_json = context.get('photo_array_json', UNDEFINED)
        enable_comments = context.get('enable_comments', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        def content():
            return render_content(context)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        title = context.get('title', UNDEFINED)
        folders = context.get('folders', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        photo_array = context.get('photo_array', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        ui = _mako_get_namespace(context, 'ui')
        enable_comments = context.get('enable_comments', UNDEFINED)
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
        translations = context.get('translations', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        len = context.get('len', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        gallery_path = context.get('gallery_path', UNDEFINED)
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
        photo_array_json = context.get('photo_array_json', UNDEFINED)
        thumbnail_size = context.get('thumbnail_size', UNDEFINED)
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
{"uri": "gallery.tmpl", "source_encoding": "utf-8", "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootstrap4/templates/gallery.tmpl", "line_map": {"128": 26, "129": 27, "130": 29, "131": 30, "132": 30, "133": 30, "134": 30, "135": 30, "136": 31, "137": 31, "138": 31, "139": 31, "140": 33, "141": 36, "142": 37, "143": 37, "149": 41, "23": 3, "26": 4, "32": 0, "161": 41, "162": 42, "163": 42, "164": 52, "165": 53, "166": 54, "167": 55, "168": 55, "169": 55, "170": 55, "171": 55, "177": 61, "185": 61, "186": 65, "187": 65, "188": 66, "189": 66, "63": 2, "64": 3, "65": 4, "195": 5, "70": 5, "75": 39, "206": 195, "80": 59, "85": 70, "91": 7, "107": 7, "108": 8, "109": 8, "110": 9, "111": 10, "112": 10, "113": 10, "114": 12, "115": 13, "116": 14, "117": 14, "118": 17, "119": 18, "120": 19, "121": 20, "122": 20, "123": 20, "124": 20, "125": 20, "126": 22, "127": 24}}
__M_END_METADATA
"""
