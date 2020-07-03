class Present {
      constructor(form) {
       this.form=form;
      // Bind event listeners.
      this._btnFunction = this._btnFunction.bind(this);
      
      this.btn=document.querySelector('.ModifProfil');
      
      form.style.display='none';
      this.btn.addEventListener('click',this._btnFunction);
      
     // this.containerElement.append(this.btn);
    } 
    _btnFunction(event){
      console.log("btn");
      const form =event.currentTarget;
      //this.form = document.querySelector('form');
      this.form.style.display='block';
      let titre = document.querySelector('h5');
      titre.innerHTML="Modifier le profil";
      document.querySelector('.activeAjout').disabled = true;
      document.querySelector(".ModifProfil").disabled = true;
      
      form.removeEventListener('click',this._btnFunction);
    }
  }
  
  
  