var preUrl = "http://lowcost-env.xjjzsdshyn.us-east-1.elasticbeanstalk.com"
var app = angular.module('myapp',['ngAnimate', 'ngSanitize', 'ui.bootstrap'])
app.controller('MyController', MainCtrl);

function MainCtrl($http, $scope, $interval){
    $scope.init = function(){
      $scope.oldwords = ["res50"];
      $scope.words = {};
      $scope.hideupdate = true;
    };
    $scope.goLogin = function() {
      window.location = "login.html";
    }
    
};



