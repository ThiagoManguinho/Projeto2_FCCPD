while true; do
    echo "Fazendo requisição para o servidor"
    curl -s http://server:8080
    echo ""
    sleep 5
done