 form = document.querySelector('#ModifProfil');
 present = new Present(form);
 ajout = document.querySelector('.activeAjout');
 ajout.addEventListener('click',ajouter);
 
 function annulerModif() {
    let form = document.querySelector('#ModifProfil');
    form.style.display = "none";
    let titre = document.querySelector('h5');
    titre.innerHTML="";
    document.querySelector('.activeAjout').disabled = false;
    document.querySelector(".ModifProfil").disabled = false;
    ajout.addEventListener('click',ajouter);
    present = new Present(form);
  }
  function annuler() {
    let form = document.querySelector('form');
    form.style.display = "none";
    let titre = document.querySelector('h5');
    titre.innerHTML="";
    document.querySelector('.activeAjout').disabled = false;
    document.querySelector(".ModifProfil").disabled = false;
    ajout.addEventListener('click',ajouter);
    present = new Present(form);
  }
  function ajouter() {
    let form = document.querySelector('form');
    let titre = document.querySelector('h5');
    titre.innerHTML="Ajouter une recette";
    form.style.display = "block";
   
    document.querySelector('.activeAjout').disabled = true;
    document.querySelector(".ModifProfil").disabled = true;

    console.log("annuler");
  }
  

