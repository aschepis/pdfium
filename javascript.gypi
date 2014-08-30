{
  'targets': [
    {
      'target_name': 'javascript',
      'type': 'static_library',
        'include_dirs': [
          '<(DEPTH)/v8',
          '<(DEPTH)/v8/include',
        ],
      'dependencies': [
        '<(DEPTH)/v8/tools/gyp/v8.gyp:v8',
        '<(DEPTH)/v8/tools/gyp/v8.gyp:v8_libplatform'
      ],
      'export_dependent_settings': [
        '<(DEPTH)/v8/tools/gyp/v8.gyp:v8',
      ],
      'ldflags': [ '-L<(PRODUCT_DIR)',],
      'sources': [
        'fpdfsdk/include/javascript/app.h',
        'fpdfsdk/include/javascript/color.h',
        'fpdfsdk/include/javascript/console.h',
        'fpdfsdk/include/javascript/Consts.h',
        'fpdfsdk/include/javascript/Document.h',
        'fpdfsdk/include/javascript/event.h',
        'fpdfsdk/include/javascript/Field.h',
        'fpdfsdk/include/javascript/global.h',
        'fpdfsdk/include/javascript/Icon.h',
        'fpdfsdk/include/javascript/IJavaScript.h',
        'fpdfsdk/include/javascript/JavaScript.h',
        'fpdfsdk/include/javascript/JS_Console.h',
        'fpdfsdk/include/javascript/JS_Context.h',
        'fpdfsdk/include/javascript/JS_Define.h',
        'fpdfsdk/include/javascript/JS_EventHandler.h',
        'fpdfsdk/include/javascript/JS_GlobalData.h',
        'fpdfsdk/include/javascript/JS_Module.h',
        'fpdfsdk/include/javascript/JS_Object.h',
        'fpdfsdk/include/javascript/JS_Runtime.h',
        'fpdfsdk/include/javascript/JS_Value.h',
        'fpdfsdk/include/javascript/PublicMethods.h',
        'fpdfsdk/include/javascript/report.h',
        'fpdfsdk/include/javascript/resource.h',
        'fpdfsdk/include/javascript/util.h',
        'fpdfsdk/src/javascript/app.cpp',
        'fpdfsdk/src/javascript/color.cpp',
        'fpdfsdk/src/javascript/console.cpp',
        'fpdfsdk/src/javascript/Consts.cpp',
        'fpdfsdk/src/javascript/Document.cpp',
        'fpdfsdk/src/javascript/event.cpp',
        'fpdfsdk/src/javascript/Field.cpp',
        'fpdfsdk/src/javascript/global.cpp',
        'fpdfsdk/src/javascript/Icon.cpp',
        'fpdfsdk/src/javascript/JS_Context.cpp',
        'fpdfsdk/src/javascript/JS_EventHandler.cpp',
        'fpdfsdk/src/javascript/JS_GlobalData.cpp',
        'fpdfsdk/src/javascript/JS_Object.cpp',
        'fpdfsdk/src/javascript/JS_Runtime.cpp',
        'fpdfsdk/src/javascript/JS_Value.cpp',
        'fpdfsdk/src/javascript/PublicMethods.cpp',
        'fpdfsdk/src/javascript/report.cpp',
        'fpdfsdk/src/javascript/util.cpp',
      ],
    },
    {
      'target_name': 'jsapi',
      'type': 'static_library',
      'dependencies': [
        '<(DEPTH)/v8/tools/gyp/v8.gyp:v8',
      ],
      'export_dependent_settings': [
        '<(DEPTH)/v8/tools/gyp/v8.gyp:v8',
      ],
      'include_dirs': [
        '<(DEPTH)/v8',
        '<(DEPTH)/v8/include',
      ],
      'ldflags': [ '-L<(PRODUCT_DIR)',],
      'sources': [
        'fpdfsdk/include/jsapi/fxjs_v8.h',
        'fpdfsdk/src/jsapi/fxjs_v8.cpp',
      ],
    }
  ]
}
