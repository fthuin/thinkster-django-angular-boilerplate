(function() {
    'use strict';

    angular
        .module('thinkster.routes')
        .config(config);

    config.$inject = ['$stateProvider', '$urlRouterProvider'];

    /**
     * @name config
     * @desc Define valid application routes
     */
    function config($stateProvider, $urlRouterProvider) {

        $stateProvider.state('register', {
                url: '/register',
                controller: 'RegisterController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/authentication/register.html'
            })
            .state('login', {
                url: '/login',
                controller: 'LoginController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/authentication/login.html'
            })
            .state('home', {
                url: '/',
                controller: 'IndexController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/layout/index.html'
            })
            .state('profile', {
                url: '/+{username}',
                controller: 'ProfileController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/profiles/profile.html'
            })
            .state('userSettings', {
                url: '/+{username}/settings',
                controller: 'ProfileSettingsController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/profiles/settings.html'
            })
        $urlRouterProvider.otherwise('/');
    }
})();
