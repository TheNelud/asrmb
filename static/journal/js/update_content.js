function showDiv(id) {
  var all = document.querySelectorAll(".sidebar-of-text");
  for (var i = 0; i < all.length; i++) {
    if (all[i].id === id) {
      all[i].style.display = (all[i].style.display === 'none')? 'block' : 'none';
    } else {
      all[i].style.display = 'none';
    }
  }
}

function showDivContent(id_content){
  var all = document.querySelectorAll(".content_text");
  for (var i = 0; i < all.length; i++) {
    if (all[i].id === id_content) {
      all[i].style.display = (all[i].style.display === 'none')? 'block' : 'none';
    } else {
      all[i].style.display = 'none';
    }
  }
}

async function updateDivContent(selector) {
  try {
    var html = await (await fetch(location.href)).text();
    var newdoc = new DOMParser().parseFromString(html, 'text/html');
    document.querySelector(selector).outerHTML = newdoc.querySelector(selector).outerHTML;
    console.log('Элемент '+selector+' был успешно обновлен');
    showDivContent(selector);
    document.querySelector(selector).style.display="block";
    return true;
  } catch(err) {
    console.log('При обновлении элемента '+selector+' произошла ошибка:');
    console.error(err);
    return false;
  }
}


// async function updateDivContent(selector){
//   $(selector).on('click', function(e){  e.preventDefault();$(this).closest('ul').next('.box').toggleClass('active');})
// }




