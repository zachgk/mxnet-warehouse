var preUrl = "http://127.0.0.1:5000";
var app = angular.module('myapp', ['ui.bootstrap']);
app.controller('MyController', MainCtrl);

function MainCtrl($http, $scope, $interval) {
    $scope.init = function() {
    };
    $scope.goSearch = function() {
        window.location = "index.html";
    }
}