import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Progress } from "@/components/ui/progress";
import { Upload } from "lucide-react";

export default function ResumeRating() {
  const [loading, setLoading] = useState(false);
  const [selectedRole, setSelectedRole] = useState("");
  const [skillsScore, setSkillsScore] = useState(null);
  const [projectScore, setProjectScore] = useState(null);
  const [certificationScore, setCertificationScore] = useState(null);
  const [grammarScore, setGrammarScore] = useState(null);
  const [totalScore, setTotalScore] = useState(null);
  const [feedback, setFeedback] = useState("");
  const [detailedSuggestions, setDetailedSuggestions] = useState("");

  const roles = {
    "Software Engineer": ["Java", "Python", "Data Structures", "Algorithms", "Git"],
    "Frontend Developer": ["HTML", "CSS", "JavaScript", "React", "UI/UX"],
    "Backend Developer": ["Node.js", "SQL", "MongoDB", "API", "Docker"],
    "Data Scientist": ["Python", "Machine Learning", "Pandas", "TensorFlow", "SQL"],
    "DevOps Engineer": ["AWS", "Kubernetes", "Docker", "CI/CD", "Terraform"],
    "Full Stack Developer": ["React", "Node.js", "MongoDB", "GraphQL", "TypeScript"],
    "Cloud Engineer": ["Azure", "AWS", "GCP", "Kubernetes", "Terraform"],
    "Cybersecurity Analyst": ["Network Security", "Penetration Testing", "SIEM", "Ethical Hacking", "Encryption"],
    "AI/ML Engineer": ["Deep Learning", "NLP", "TensorFlow", "PyTorch", "Computer Vision"],
    "Blockchain Developer": ["Ethereum", "Solidity", "Smart Contracts", "Web3.js", "Cryptography"],
    "Other": []
  };

  const handleUpload = (event) => {
    const file = event.target.files[0];
    if (file && selectedRole) {
      setLoading(true);
      setTimeout(() => {
        const keywords = roles[selectedRole] || [];
        const matchedKeywords = Math.floor(Math.random() * keywords.length);
        const skillsScore = Math.floor((matchedKeywords / keywords.length) * 100);
        const projectScore = Math.floor(Math.random() * 100);
        const certificationScore = Math.floor(Math.random() * 100);
        const grammarScore = Math.floor(Math.random() * 100);
        const totalScore = Math.floor((skillsScore + projectScore + certificationScore + grammarScore) / 4);

        let feedbackMsg = "";
        let suggestions = "";

        if (totalScore < 50) {
          feedbackMsg = "Your resume needs significant improvement. Work on the key areas mentioned below.";
          suggestions = `\n- Improve your skill section by adding more relevant technologies like ${keywords.join(", ")}.\n- Enhance your project descriptions with clear impact statements and technologies used.\n- Consider earning more relevant certifications.\n- Proofread your resume to correct grammatical mistakes.`;
        } else if (totalScore < 80) {
          feedbackMsg = "Your resume is good but can be improved further. See suggestions below.";
          suggestions = `\n- Strengthen your skills by adding more projects showcasing ${keywords.join(", ")}.\n- Include measurable achievements in your project descriptions.\n- List additional certifications related to your role.\n- Make sure your resume is free from grammatical errors.`;
        } else {
          feedbackMsg = "Great job! Your resume is well-optimized for the selected role.";
          suggestions = "\n- Keep updating your resume with new projects and certifications.\n- Stay updated with industry trends to remain competitive.";
        }

        setSkillsScore(skillsScore);
        setProjectScore(projectScore);
        setCertificationScore(certificationScore);
        setGrammarScore(grammarScore);
        setTotalScore(totalScore);
        setFeedback(feedbackMsg);
        setDetailedSuggestions(suggestions);
        setLoading(false);
      }, 2000);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <Card className="w-full max-w-lg p-6 shadow-xl">
        <CardContent className="flex flex-col items-center space-y-4">
          <h1 className="text-2xl font-bold">Resume ATS Score Checker</h1>
          <p className="text-gray-600">Select a role and upload your resume to get an ATS-friendly score.</p>
          
          <select 
            className="w-full p-2 border border-gray-300 rounded-lg" 
            value={selectedRole} 
            onChange={(e) => setSelectedRole(e.target.value)}
          >
            <option value="">Select a Tech Role</option>
            {Object.keys(roles).map((role, index) => (
              <option key={index} value={role}>{role}</option>
            ))}
          </select>
          
          <label className={`cursor-pointer bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-lg flex items-center space-x-2 ${!selectedRole ? 'opacity-50 cursor-not-allowed' : ''}`}>
            <Upload size={18} />
            <span>Upload Resume</span>
            <input 
              type="file" 
              accept=".pdf,.docx" 
              className="hidden" 
              onChange={handleUpload} 
              disabled={!selectedRole} 
            />
          </label>
          
          {loading && <p className="text-gray-500">Analyzing your resume...</p>}
          {totalScore !== null && (
            <div className="w-full">
              <p className="text-lg font-semibold text-center">Total Resume Score: {totalScore}/100</p>
              <Progress value={totalScore} className="h-3 mt-2" />
              <p className="text-sm text-gray-700 mt-2">{feedback}</p>
              <p className="text-md font-semibold mt-4">Detailed Suggestions:</p>
              <p className="text-sm text-gray-700 whitespace-pre-wrap">{detailedSuggestions}</p>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
