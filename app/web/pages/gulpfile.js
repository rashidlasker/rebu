/**
 * Gulp file to automate the various tasks
 */

var autoprefixer = require('gulp-autoprefixer');
var browserSync = require('browser-sync').create();
var csscomb = require('gulp-csscomb');
var cleanCss = require('gulp-clean-css');
var cache = require('gulp-cache');
var cssnano = require('gulp-cssnano');
var del = require('del');
var imagemin = require('gulp-imagemin');
var htmlPrettify = require('gulp-html-prettify');
var gulp = require('gulp');
var gulpIf = require('gulp-if');
var gulpRun = require('gulp-run');
var gulpUtil = require('gulp-util');
var npmDist = require('gulp-npm-dist');
var postcss = require('gulp-postcss');
var runSequence = require('run-sequence');
var sass = require('gulp-sass');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var useref = require('gulp-useref-plus');
var wait = require('gulp-wait');

// Define paths

var paths = {
    dist: {
        base: 'static/pages',
        img:  'static/pages/img',
        libs: 'static/pages/vendor'
    },
    base: {
        base: './',
        node: 'node_modules'
    },
    src: {
        base: './',
        css:  'static/pages/css',
        html: '**/*.html',
        img:  'static/pages/img/**/*.+(png|jpg|gif|svg)',
        js:   'static/pages/js/**/*.js',
        scss: 'static/pages/scss/**/*.scss'
    }
}

// Compile SCSS

gulp.task('scss', function() {
  return gulp.src(paths.src.scss)
    .pipe(wait(500))
    .pipe(sass().on('error', sass.logError))
    .pipe(postcss([require('postcss-flexbugs-fixes')]))
    .pipe(autoprefixer({
        browsers: ['> 1%']
    }))
    .pipe(csscomb())
    .pipe(gulp.dest(paths.src.css))
    .pipe(browserSync.reload({
        stream: true
    }));
});

// Minify CSS

gulp.task('minify:css', function() {
  return gulp.src([
        paths.src.css + '/argon.css'
    ])
    .pipe(cleanCss())
    .pipe(rename({ suffix: '.min' }))
    .pipe(gulp.dest(paths.dist.base + '/css'))
});

// Minify JS

gulp.task('minify:js', function(cb) {
    return gulp.src([
            paths.src.base + '/static/pages/js/argon.js'
        ])
        .pipe(uglify())
        .pipe(rename({ suffix: '.min' }))
        .pipe(gulp.dest(paths.dist.base + '/js'))
});

// Build

gulp.task('default', function(callback) {
    runSequence('scss', 'minify:js', 'minify:css',
        callback);
});
