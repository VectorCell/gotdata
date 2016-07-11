// MADE FOR TESTING PURPOSES; CURRENTLY UNUSED

var app = angular.module("got_app", []);

app.controller("character_ctrl", function($scope, $http) {
    $http.get("http://gotdata.me/query=characters")
    .then(function (response) {
        $scope.character = response.data[0];
    });
});