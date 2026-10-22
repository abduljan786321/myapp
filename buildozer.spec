[app]
title = MyApp
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,charset_normalizer==2.1.1
orientation = portrait
fullscreen = 0
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
android.skip_update = False
android.build_tools_version = 34.0.0
