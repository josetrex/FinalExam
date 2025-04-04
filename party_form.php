<!DOCTYPE html>
<html>
<head>
    <title>Digital Party Planner Form</title>
</head>
<body>
    <h2>🎉 Plan Your Party 🎉</h2>
    <form action="party_planner.py" method="get">
        <?php
            $party_items = [
                0 => "Cake",
                1 => "Balloons",
                2 => "Music System",
                3 => "Lights",
                4 => "Catering Service",
                5 => "DJ",
                6 => "Photo Booth",
                7 => "Tables",
                8 => "Chairs",
                9 => "Drinks",
                10 => "Party Hats",
                11 => "Streamers",
                12 => "Invitation Cards",
                13 => "Party Games",
                14 => "Cleaning Service"
            ];

            foreach ($party_items as $index => $name) {
                echo "<input type='checkbox' name='items[]' value='$index'> $index: $name<br>";
            }
        ?>
        <br>
        <input type="submit" value="Generate Party Code">
    </form>

    <script>
      
        document.querySelector('form').addEventListener('submit', function (e) {
            const checkboxes = document.querySelectorAll('input[name="items[]"]:checked');
            const values = Array.from(checkboxes).map(cb => cb.value);
            const input = document.createElement('input');
            input.type = 'hidden';
            input.name = 'items';
            input.value = values.join(',');
            this.appendChild(input);
        });
    </script>
</body>
</html>