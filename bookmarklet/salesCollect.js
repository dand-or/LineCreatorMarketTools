javascript:
var items = document.querySelectorAll("tr.ng-scope");
var total = 0;
var salesItems = [];
for (var item of items) {
    var itemName = item.children[0].innerText;
    var sales = parseInt(item.children[1].innerText.replace("¥ ", ""));
    if (sales > 0) {
        total += sales;
        var dict = {};
        dict[itemName] = sales;
        salesItems.push(dict);
        var checkbox = item.querySelector("input");
        if (!checkbox.checked) {
            checkbox.click();
        }
    }
}
var result = "total: " + total + "\n";
salesItems.forEach(salesItem => {
    var keys = Object.keys(salesItem);
    var key = keys[0];
    result += key + ": " + salesItem[key] + "\n";
});

alert(result);