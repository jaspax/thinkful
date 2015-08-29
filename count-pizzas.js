var file = process.argv[2];
var fs = require("fs");
fs.readFile(file, 'utf8', function(err, data) {
    if (err) throw err;
    
    var pizzaList = JSON.parse(data);
    var pizzaCount = {};
    pizzaList.forEach(function(pizza) {
        var key = pizza.toppings.sort().join(", ");
        pizzaCount[key] = pizzaCount[key] ? pizzaCount[key] + 1 : 1;
    });
    
    var pizzaSorted = Object.keys(pizzaCount).map(function(key) { 
            return { pizza: key, count: pizzaCount[key] };
        }).sort(function(pizzaA, pizzaB) {
            return pizzaB.count - pizzaA.count;
        });
        
    for (var i = 0; i < pizzaSorted.length && i < 20; i++) {
        console.log("%s: %d", pizzaSorted[i].pizza, pizzaSorted[i].count);
    }
});