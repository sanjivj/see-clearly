# This batch file gathers the templates from the cartridge package,
# and places them in a new theme app.
if ($# < 2)
    $2 = 'theme'

# Create the theme app and fetch the base.html from Mezzanine.
python manage.py startapp $2
python manage.py collecttemplates -t base.html

# Create static and template directories in theme.
cd $2
mkdir static
cd static
mkdir css
mkdir js
cd ..
mkdir templates
cd ..

# Place the static and templates in those directories.
if ($# > 0)
    cp $1/*.html $2/templates
    cp $1/css/*.css $2/static/css
    cp $1/js/* $2/static/js

# Finally, add base.html to theme's templates and enter the theme directory.
cp templates/base.html $2/templates
cd $2
