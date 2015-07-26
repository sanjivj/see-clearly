# This batch file gathers the templates file from a Cartridge package,
# and places them in a theme app.
var inputz = $#
if[inputz < 2] then
    $2 = 'theme'

# Create the theme app and fetch the base.html file from Mezzanine.
python manage.py startapp $2
python manage.py collecttemplates -t base.html

# Create static and template directories in theme.
cd $2
mkdir static
cd static
mkdir css
mkdir js
mkdir img
cd ..
mkdir templates
cd ..

# Place the static files and templates in those directories.
if[$# > 0] then
    cp $1/*.html $2/templates
    cp -r $1/css/* $2/static/css
    cp -r $1/js/* $2/static/js
    cp -r $1/img/* $2/static/img


# Finally, add base.html to theme's templates and enter the theme directory.
cp templates/base.html $2/templates
cd  $2
