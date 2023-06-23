class API:
    def __init__(self):
        self.expressions = ""

    def SetExpressionNote(self, id : str, text : str):
        self.expressions += "    calculator.setExpression({ id: '" + id + "', type: \'text\', text: '" + text + "' });\n"

    def SetExpression(self, id : str, latex : str):
        self.expressions += "    calculator.setExpression({ id: '" + id + "', latex: '" + latex + "' });\n"

    def Compile(self, fileName : str):
        baseHtml = """<script src="https://www.desmos.com/api/v1.8/calculator.js?apiKey=dcb31709b452b1cf9dc26972add0fda6"></script>
<div id="calculator" style="width: 1920px; height: 1080px;"></div>
<script>
    var elt = document.getElementById('calculator');
    var calculator = Desmos.GraphingCalculator(elt);
{}
</script>
        """

        f = open(fileName, "w")
        f.write(baseHtml.format(self.expressions))
        f.close()