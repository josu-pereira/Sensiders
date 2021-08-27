const nodemailer = require('nodemailer');
const transport = nodemailer.createTransport({
    host: "smtp.live.com",
    secureConnection: false,
    port: 587,
    auth: {
        user: "201grupo11c@bandtec.com.br",
        pass: "#Gfgrupo11c"
    }, 
    tls: {
        ciphers: 'SSLv3'
    }
});

module.exports = transport;