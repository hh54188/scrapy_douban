module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        uglify: {
            build: {
                files: [
                    {
                        src: ['src/bower_components/jquery/jquery.min.js', 'src/bower_components/bootstrap/docs/assets/js/bootstrap.min.js'],
                        dest: 'build/js/lib.min.js'  
                    }, 
                    {
                        src: ['src/js/script.js'],
                        dest: 'build/js/script.min.js'
                    }
                ]
            }
        },
        cssmin: {
            build: {
                files: [
                    {
                        src: ['src/bower_components/bootstrap/docs/assets/css/bootstrap.css', 'src/css/style.css'],
                        dest: 'build/css/style.min.css'
                    }                
                ]
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-cssmin');

    grunt.registerTask('default', ['uglify', 'cssmin']);
};