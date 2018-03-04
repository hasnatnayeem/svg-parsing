<?php
$directory = 'files/';
$files = array_slice(scandir($directory), 2);

?>
<!DOCTYPE html>
<html>
<head>
	<title></title>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.3/jquery.min.js"></script>
</head>
<body>
    <center>
	    <select id="file-name">
		    <option>Select file</option>
		    <?php foreach ($files as $file) { ?>
			    <option value="<?=$file?>"><?=$file?></option>
		    <?php } ?>
	    </select>
    </center>

    <div id = "result"></div>

</body>

<script>
	$(document).ready(function(){
		$('#file-name').change(function(){
			var file = $(this).val();
            $.ajax({url: "api.php?f=" + file, success: function(result){
                $("#result").html(result);
            }});
		});
	});
</script>
</html>
