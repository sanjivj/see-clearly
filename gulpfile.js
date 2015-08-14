var gulp = require('gulp');
var lint = require('gulp-jshint');
var rename = require('gulp-rename');
var mocha = require('gulp-mocha');
var istanbul = require('gulp-istanbul');
var minifyCSS = require('gulp-minify-css');
var livereload = require('gulp-livereload');
var shell = require('gulp-shell');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var imagemin = require('gulp-imagemin');

//This files are required for testing ruby-2.1.5 compatiblility
var del = require('del');
var auto = require('gulp-autoprefixer');
var gzip = require('gulp-gzip');
var plumber = require('gulp-plumber');
var sass = require('gulp-sass');
var util = require('gulp-util');

var paths = {
    scripts: ['./SimpleGifts/assets/js/*.js'],
    styles:  ['./SimpleGifts/assets/css/*.css', './SimpleGifts/assets/css/rgs_css/*.css'],
    images:  ['./SimpleGifts/assets/img/**/*'],
    pages:   ['./SimpleGifts/templates/*']
};

// Not all tasks need to use streams
// A gulpfile is just another node program and you can use all packages available on npm
gulp.task('clean', function(cb) {
  // You can use multiple globbing patterns as you would with `gulp.src`
  del(['./SimpleGifts/static/css/*.css ./SimpleGifts/static/js/*.js'], cb);
});


gulp.task('brew', function () {
	return gulp.src(['./SimpleGifts/assets/js/test/*.js'], {read: false})
		.pipe(mocha({reporter: 'nyan'}));
});

gulp.task('test', function (cb) {
  //gulp.src(['lib/**/*.js', 'test.js'])
    gulp.src(['./SimpleGifts/assets/js/test/*.js'])
    .pipe(istanbul()) // Covering files
    .pipe(istanbul.hookRequire()) // Force `require` to return covered files
    .on('finish', function () {
      gulp.src(['test/*.js'])
        .pipe(mocha())
        .pipe(istanbul.writeReports()) // Creating the reports after tests runned
        .on('end', cb);
    });
});

//With gulp css and gulp styles, there is no need to use the django collectstatic method.
//gulp.task('collectstatic',
    //shell.task(['manage.py collectstatic'])
//);

//TODO:check on SOF for reason why 404 error for static files.

gulp.task('scripts', ['clean'], function() {
  // Minify and copy all JavaScript (except vendor scripts)
  // with sourcemaps all the way down
  return gulp.src(paths.scripts)
    .pipe(lint())
    .pipe(lint.reporter('default'))
    .pipe(mocha())
      .pipe(uglify())
      .pipe(concat('all.min.js'))
    .pipe(gulp.dest('./SimpleGifts/static/js'))
    .pipe(livereload());
});


gulp.task('styles', ['clean'], function(){
    return gulp.src(paths.styles)
        .pipe(minifyCSS())
        .pipe(rename({extname:'.min.css'}))
        .pipe(gulp.dest('./SimpleGifts/static/css'))
        .pipe(livereload());
});

gulp.task('css', function(){
    return gulp.src('./node_modules/titon-toolkit/scss/**.scss')
        .pipe(sass())
        .pipe(gulp.dest('./SimpleGifts/assets/css'))
});

gulp.task('pages', function(){
    return gulp.src(paths.pages)
        .pipe(gulp.dest('./SimpleGifts/templates'))
        .pipe(livereload());
});


gulp.task('default',
    ['watch', 'django']
);

gulp.task('django',
    shell.task(['python manage.py runserver'])
);

gulp.task('watch', function(){
    livereload.listen();
    gulp.watch('./SimpleGifts/assets/css/*.css', ['styles']);
    gulp.watch('./SimpleGifts/assets/js/*.js', ['scripts']);
    gulp.watch('./SimpleGifts/templates/*.html', ['pages']);
});
