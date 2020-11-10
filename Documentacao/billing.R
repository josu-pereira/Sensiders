juros = 51.66
for(i in seq(1:4)) {
    juros <- c(juros, ((51.66*(i+1))*(1+0.03)**i))
}
juros
barplot(juros, main = "relação de juros aplicados ao billing mensal", ylab = "preço", xlab = "meses")
