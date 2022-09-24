var playerName=document.getElementById("productName");
var totalScore=document.getElementById("productPrice");
var categoryPlayer=document.getElementById("productCategory");
var searchProduct=document.getElementById("searchInput");
var productlist=[];

function addProduct(){
var product = {
    Name:playerName.value ,
    score:totalScore.value,
    category:categoryPlayer.value,
}
productlist.push(product);
}
function displayData() {
    var temp=""
    for(var i=0;i<productlist.length;i++){
    temp+=`
    <tr>
    <td>`+i+`</td>
    <td>`+productlist[i].Name+`</td>
    <td>`+productlist[i].price+`</td>
    <td>`+productlist[i].category+`</td>
    <td>
        <button type="button" class="btn btn-outline-danger onclick="addProduct(`+i+`)">Add Player</button>
    </td>
    <td>
        <button type="button" class="btn btn-outline-primary"onclick="Deletex(`+i+`)">Delete Player</button>
    </td>
  
</tr>
    `
    }
    document.getElementById("tableBody").innerHTML=temp;
}
function Deletex(x){
console.log(x);
productlist.splice(x,1);
displayData();
console.log(productlist);
}
// function updateForm() {
//    NameProduct.value="";
//    priceProduct.value="";
//    categoryProduct.value="";
//    DescProduct.value="";
// }
// function updateProduct(x) {
//     NameProduct.value=productlist[x];
// }
function search() {
    var searchValue=searchProduct.value .toLowerCase()
        var temp=""
        for(var i=0;i<productlist.length;i++){
            if(productlist[i].Name.toLowerCase().includes(searchValue)==true){
        temp+=`
        <tr>
        <td>`+i+`</td>
        <td>`+productlist[i].Name+`</td>
        <td>`+productlist[i].price+`</td>
        <td>`+productlist[i].category+`</td>
        <td>`+productlist[i].Desc+`</td>
        <td>
            <button type="button" class="btn btn-outline-danger onclick="updateProduct(`+i+`)">Update</button>
        </td>
        <td>
            <button type="button" class="btn btn-outline-primary"onclick="Deletex(`+i+`)">Delete</button>
        </td>
      
    </tr>
        `
        }
    }
        document.getElementById("tableBody").innerHTML=temp;
    }