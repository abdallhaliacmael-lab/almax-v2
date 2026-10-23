[app]

# (str) Title of your application
title = Almax 2.0

# (str) Package name
package.name = almax

# (str) Package domain (needed for android packaging)
package.domain = org.almax

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) Application requirements
# ركز هنا: أضفنا الحزم الأساسية التي يحتاجها تطبيقك
requirements = python3,kivy

# (str) Supported orientation (landscape, portrait, all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
