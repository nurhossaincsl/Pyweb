from IPython.display import HTML

resume_html = """
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>My Resume</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f7f6;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 30px auto;
            background: #fff;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        header {
            text-align: center;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }
        header h1 {
            margin: 0;
            color: #2c3e50;
            font-size: 2.5em;
        }
        header p {
            margin: 5px 0;
            color: #7f8c8d;
            font-size: 1.1em;
        }
        .contact-info {
            margin-top: 10px;
            font-size: 0.9em;
            color: #555;
        }
        .contact-info span {
            margin: 0 10px;
        }
        section {
            margin-bottom: 30px;
        }
        h2 {
            color: #2980b9;
            border-bottom: 1px solid #d1d5db;
            padding-bottom: 5px;
            margin-bottom: 15px;
        }
        .job, .education {
            margin-bottom: 20px;
        }
        .job-title, .edu-title {
            font-weight: bold;
            font-size: 1.1em;
            color: #2c3e50;
        }
        .company, .school {
            font-style: italic;
            color: #7f8c8d;
        }
        .date {
            float: right;
            color: #95a5a6;
            font-size: 0.9em;
        }
        .skills-list {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            padding: 0;
            list-style: none;
        }
        .skills-list li {
            background: #e1f5fe;
            color: #0288d1;
            padding: 6px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: 500;
        }
        .clearfix::after {
            content: "";
            clear: both;
            display: table;
        }
    </style>
</head>
<body>
    <div class='container'>
        <header>
            <h1>John Doe</h1>
            <p>Professional Web Developer & Data Analyst</p>
            <div class='contact-info'>
                <span>📧 email@example.com</span> |
                <span>📱 (123) 456-7890</span> |
                <span>🌐 linkedin.com/in/johndoe</span>
            </div>
        </header>

        <section>
            <h2>Summary</h2>
            <p>Result-driven professional with over 5 years of experience building responsive web applications and analyzing complex datasets. Proven track record of collaborating with cross-functional teams to deliver scalable digital solutions.</p>
        </section>

        <section>
            <h2>Experience</h2>
            <div class='job'>
                <div class='clearfix'>
                    <span class='job-title'>Senior Developer</span>
                    <span class='date'>2021 - Present</span>
                </div>
                <div class='company'>Tech Solutions Inc.</div>
                <p>Lead a team of 4 developers to build modern web solutions using React and Python. Improved application load speed by 40% through code optimization and lazy loading.</p>
            </div>
            <div class='job'>
                <div class='clearfix'>
                    <span class='job-title'>Web Developer</span>
                    <span class='date'>2018 - 2021</span>
                </div>
                <div class='company'>Creative Web Agency</div>
                <p>Designed and maintained responsive client websites. Collaborated closely with UI/UX designers to implement clean, pixel-perfect user interfaces.</p>
            </div>
        </section>

        <section>
            <h2>Education</h2>
            <div class='education'>
                <div class='clearfix'>
                    <span class='edu-title'>B.S. in Computer Science</span>
                    <span class='date'>2014 - 2018</span>
                </div>
                <div class='school'>State University</div>
            </div>
        </section>

        <section>
            <h2>Skills</h2>
            <ul class='skills-list'>
                <li>HTML5 / CSS3</li>
                <li>JavaScript (ES6+)</li>
                <li>Python</li>
                <li>SQL</li>
                <li>React.js</li>
                <li>Git & GitHub</li>
            </ul>
        </section>
    </div>
</body>
</html>
"""

HTML(resume_html)
