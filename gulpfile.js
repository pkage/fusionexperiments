// get gulp in here
var gulp = require('gulp');

// load in our modules
var jshint = require('gulp-jshint'); // lint javascript!
var uglify = require('gulp-uglify'); // uglify!
var concat = require('gulp-concat'); // concatenate files!
var sass = require('gulp-sass'); // compile sass!
var rename = require('gulp-rename'); // rename files
var serve = require('gulp-serve'); // serve stuff!
var autoprefixer = require('gulp-autoprefixer'); // prefix css
var gutil = require('gulp-util'); // logging, etc.
var dedupe = require('gulp-dedupe'); // de-duplicate css
var cleancss = require('gulp-clean-css'); // clean resulting css
var request = require('request'); // get hot reloads going
var mkdirs = require('mkdirs'); // safe mkdirs
var exec = require('child_process').exec; // get an executor
var exit = require('gulp-exit');

var runCommand = function(command) {
	exec(command, function(err, stdout, stderr) {
		console.log(stdout);
		console.log(stderr);
		if (err !== null) {
			console.log('exec err: ' + err);
		}
	});
};

// compile scss
gulp.task('scss', function() {
	return gulp.src('app/scss/main.scss')
				.pipe(sass())
				.on('error', gutil.log)
				.pipe(autoprefixer())
				.on('error', gutil.log)
				.pipe(rename('main.css'))
				.pipe(gulp.dest('app/static/css/'))
				.pipe(dedupe())
				.pipe(cleancss())
				.pipe(rename('main.min.css'))
				.pipe(gulp.dest('app/static/css/'))
});

// compile js
gulp.task('scripts', function() {
	return gulp.src('src/js/*.js')
				.pipe(concat('index.js'))
				.on('error', gutil.log)
				.pipe(gulp.dest('.'))
				.pipe(rename('index.min.js'))
				.pipe(uglify())
				.on('error', gutil.log)
				.pipe(gulp.dest('.'));
});

// tell our reloader to reload
gulp.task('notify', function() {
	return request('http://localhost:8080/api/debug/reload');
});

// watcher task
gulp.task('watch', function() {
	gulp.watch('app/scss/*', ['scss', 'notify']);
	gulp.watch('ap/static/*', ['notify']);
});

gulp.task('mongo-start', function() {
	var command = "mongod --fork --dbpath db/ --logpath /dev/null";
	mkdirs("db/");
	runCommand(command);
});

gulp.task('mongo-stop', function() {
	var command = 'mongo admin --eval "db.shutdownServer();"';
	runCommand(command);
});

gulp.task('default', [
	'scss',
	'watch',
]);
