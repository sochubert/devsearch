let alertWrapper=document.querySelector('.alert')
let alertClose=document.querySelector('.alert__close')
 
if(alertWrapper){
  alertClose.addEventListener("click", ()=>{
    console.log("Clicked!")
    alertWrapper.style.display='none'
  })
}