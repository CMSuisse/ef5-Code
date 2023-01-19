function calculate(){
    var number_1 = document.getElementById("number-1").value;
    var number_2 = document.getElementById("number-2").value;
    var number_3 = document.getElementById("number-3").value;
    var solution = document.getElementById("solution");

    var relation_number_1_to_number_2 = number_2/number_1;
    var solution_number = number_3 * relation_number_1_to_number_2;
    console.log(solution_number);
    solution.value = solution_number;
}