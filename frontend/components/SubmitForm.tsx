import { useForm } from "react-hook-form";

interface FormData {
  name: string;
  email: string;
  message: string;
}

const SubmitForm: React.FC = () => {
  const { register, handleSubmit, formState: { errors } } = useForm<FormData>();

  // Function to handle form submission
  const onSubmit = async (data: FormData) => {
    try {
      // Send POST request to your FastAPI backend
      const response = await fetch('http://localhost:8000/submit-form', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),  // Send the form data as JSON
      });

      // Handle the response
      if (response.ok) {
        const result = await response.json();
        console.log('Form successfully submitted:', result);
        alert('Form submitted successfully!');
      } else {
        console.error('Error submitting form');
        alert('Failed to submit form');
      }
    } catch (error) {
      console.error('Error occurred:', error);
      alert('An error occurred during form submission');
    }
  };

  return (
    <div className="flex justify-center items-center h-screen bg-gray-900">
      <form onSubmit={handleSubmit(onSubmit)} className="space-y-4 bg-gray-800 p-8 rounded-lg shadow-lg w-full max-w-md">
        <h2 className="text-2xl font-bold text-center text-white mb-4">Submit Your Form</h2>

        <div>
          <label className="text-white block">Name</label>
          <input
            {...register("name", { required: "Name is required" })}
            className="w-full p-2 rounded-md bg-gray-700 text-white"
            placeholder="Enter your name"
          />
          {errors.name && <p className="text-red-500 text-sm">{errors.name.message}</p>}
        </div>

        <div>
          <label className="text-white block">Email</label>
          <input
            {...register("email", { required: "Email is required" })}
            className="w-full p-2 rounded-md bg-gray-700 text-white"
            placeholder="Enter your email"
          />
          {errors.email && <p className="text-red-500 text-sm">{errors.email.message}</p>}
        </div>

        <div>
          <label className="text-white block">Message</label>
          <textarea
            {...register("message", { required: "Message is required" })}
            className="w-full p-2 rounded-md bg-gray-700 text-white"
            placeholder="Write your message"
          />
          {errors.message && <p className="text-red-500 text-sm">{errors.message.message}</p>}
        </div>

        <button
          type="submit"
          className="w-full py-2 px-4 bg-indigo-600 text-white rounded-md hover:bg-indigo-700"
        >
          Submit
        </button>
      </form>
    </div>
  );
};

export default SubmitForm;
