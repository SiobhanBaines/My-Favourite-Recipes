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
            document.getElementById('contact').reset();
        },
        function(error) {
            console.log("FAILED", error)
        });


    return false;
}


