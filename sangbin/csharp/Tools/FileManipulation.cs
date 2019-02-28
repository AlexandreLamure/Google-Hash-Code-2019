using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

namespace csharp.Tools
{
    public static class FileManipulation
    {
        public static void ReadInput(string filename)
        {
            var lines = File.ReadAllLines(filename);

        }

        public static void WriteInput(string name, IEnumerable<string> contents)
        {
            var date = DateTime.Now.ToOADate();
            var filename = $"{name}-{date}.out";
            File.WriteAllLines(filename, contents);
        }
    }
}
