var preUrl = "http://127.0.0.1:5000";
var app = angular.module('myapp', ['ui.bootstrap', 'chart.js']);
app.controller('MyController', MainCtrl);

function MainCtrl($http, $scope, $interval) {
    $scope.init = function() {
        $scope.oldwords = ["res50"];
        $scope.words = {};
        $scope.showError = false;
        $scope.showResult = false;
    };
    $scope.goLogin = function() {
        window.location = "login.html";
    };
    $scope.componentColor = function(item) {
        if(item.tags.includes("model")) {
            return "panel-success";
        } else if(item.tags.includes("operator")) {
            return "panel-info";
        } else {
            return "panel-default";
        }
    };
    $scope.searchword = function() {
        // Initialization result section
        $scope.showError = false;
        $scope.showResult = false;
        // Prepare input data
        obj = {
            "q": $scope.word
        };
        $http({
            url: preUrl + "/api/components",
            method: "GET",
            params: obj
        }).then(function(success) {
            console.log(success["data"]);
            if (success["data"]["result"].length > 0) {
                $scope.resultList = success["data"]["result"];
                $scope.resultList.sort(function(a,b) { return b.usage[b.usage.length - 1] - a.usage[a.usage.length - 1]; });
                $scope.showResult = true;
            } else {
                $scope.showError = true;
                $scope.errorMsg = "we cannot find items matching the key word: " + $scope.word;
            }
        }, function(error) {
            console.log(error);
            $scope.showError = true;
            $scope.errorMsg = "Something wrong with our server";
        });
    };
};
