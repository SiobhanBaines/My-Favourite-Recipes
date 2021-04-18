console.log("sendemail.js")
function sendMail(contactForm) {
    emailjs.send("gmail", "Recipe-Site", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "telephone": contactForm.telephone.value,
        "enquiry": contactForm.enquiry.value},
        "user_PUJoslyDgNEmzFRMQOg72"
    )
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error)
        });
        console.log(contactForm.name.value)
        console.log(contactForm.email.value)
        console.log(contactForm.telephone.value)
        console.log(contactForm.enquiry.value)
    return false;
    
}


