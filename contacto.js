document.getElementById("contactForm").addEventListener("submit", async function(e){
    e.preventDefault();

    const data={
        nombre: document.getElementById("nombre").value.trim(),
        empresa: document.getElementById("empresa").value,
        correo: document.getElementById("email").value,
        telefono: document.getElementById("telefono").value,
        mensaje: document.getElementById("mensaje").value 
    }

    if(!data.nombre||!data.correo||!data.mensaje){

    alert("Por favor completa los campos obligatorios!");
    return
    }

    try{
        const response= await fetch("http://localhost:5000/contacto",{
            method:"POST",
            headers:{
                "Content-Type": "application/json"
            },

            body: JSON.stringify(data)
        });

        const result= await response.json();

        if(!response.ok){
            throw new Error(result.error||"Error al enviar");
        }

        alert("Mensaje enviado correctamente 🚀");
        document.getElementById("contactForm").reset();
    }catch (error){
        console.error(error);

        alert("No se pudo enviar el mensaje ❌");
    }

});