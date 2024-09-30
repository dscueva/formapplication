import { useForm } from "react-hook-form";

interface FormData {
  name: string;
  email: string;
  message: string;
}

const SubmitForm: React.FC = () => {
  const { register, handleSubmit, formState: { errors } } = useForm<FormData>();

  const onSubmit = (data: FormData) => {
    console.log(data);  // You can handle the form submission logic here
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
